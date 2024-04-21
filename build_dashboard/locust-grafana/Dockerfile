FROM grafana/grafana-oss
USER root
COPY *.sh /commands/
RUN chown -R grafana /commands
RUN apk add curl jq
USER grafana
RUN if ss -tulwn | grep ':3000' > /dev/null; then echo "Port 3000 is already in use. Skipping Grafana startup." else /run.sh fi \
    && cd /commands \
    && ./grafana_setup.sh \
    && sleep 1
