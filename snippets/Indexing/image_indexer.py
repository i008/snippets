import h5py
import numpy as np
import timeit
import time


class ImageIndexer(object):
    def __init__(self, db_path, fixed_image_shape=(512, 512), buffer_size=200, num_of_images=100):
        self.db = h5py.File(db_path, mode='w')
        self.buffer_size = buffer_size
        self.num_of_images = num_of_images
        self.fixed_image_shape = fixed_image_shape
        self.image_vector_db = None
        self.image_id_db = None
        #         self.db_index = None
        self.idxs = {"index": 0}

        self.image_vector_buffer = []
        self.image_id_buffer = []

    #         self.db_index_buffer = []

    def __enter__(self):
        print "indexing {} images".format(self.num_of_images)
        self.t0 = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.image_id_buffer:
            print "writing last buffers"
            print(len(self.image_id_buffer))

            self._write_buffer(self.image_id_db, self.image_id_buffer)
            self._write_buffer(self.image_vector_db, self.image_vector_buffer)

        print "closing h5 db"
        self.db.close()
        print "indexing took {0}".format(time.time() - self.t0)

    @property
    def image_vector_size(self):
        if self.fixed_image_shape:
            return self.fixed_image_shape[0] * self.fixed_image_shape[1]
        else:
            return None

    def create_datasets(self):

        self.image_id_db = self.db.create_dataset(
            "image_ids",
            (self.num_of_images,),
            maxshape=None,
            dtype=h5py.special_dtype(vlen=unicode)

        )

        self.image_vector_db = self.db.create_dataset(
            "image_vectors",
            (self.num_of_images, self.image_vector_size),
            maxshape=(None, self.image_vector_size),
            dtype="float"
        )

    def add(self, image_name, image_vector):
        self.image_id_buffer.append(image_name)
        self.image_vector_buffer.append(image_vector)

        if None in (self.image_vector_db, self.image_id_db):
            self.create_datasets()

        if len(self.image_id_buffer) >= self.buffer_size:
            self._write_buffer(self.image_id_db, self.image_id_buffer)
            self._write_buffer(self.image_vector_db, self.image_vector_buffer)

            # increment index
            self.idxs['index'] += len(self.image_vector_buffer)

            # clean buffers
            self._clean_buffers()

    def _write_buffer(self, dataset, buf):
        print "Writing buffer {}".format(dataset)
        start = self.idxs['index']
        end = len(buf)
        dataset[start:start + end] = buf

    def _clean_buffers(self):
        self.image_id_buffer = []
        self.image_vector_buffer = []
