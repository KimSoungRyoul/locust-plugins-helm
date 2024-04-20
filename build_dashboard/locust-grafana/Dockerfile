FROM grafana/grafana-oss
USER root
COPY *.sh /commands/
RUN chown -R grafana /commands
RUN apk add curl jq
USER grafana
RUN /run.sh & sleep 20 \
    && cd /commands \
    && ./grafana_setup.sh \
    && sleep 1