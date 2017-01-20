from example_job import example_job
from rq import Queue, job
from redis import Redis


#set up queue
q = Queue(connection=Redis(),name='name_of_redis_queue')
result = q.enqueue(example_job, args=None)

result.result
result.get_id()
job.Job.fetch(job_id, connection=Redis())

# j.is_failed j.is_finished






