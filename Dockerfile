from sebp/elk:es241_l240_k461
RUN rm /etc/logstash/conf.d/30-output.conf 
ADD ls-conf.conf /etc/logstash/conf.d/ls-conf.conf




