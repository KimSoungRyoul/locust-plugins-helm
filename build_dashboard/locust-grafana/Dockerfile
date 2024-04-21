FROM grafana/grafana-oss as builder
USER root
COPY *.sh /commands/
RUN chown -R grafana /commands
RUN apk add curl jq
USER grafana
RUN /run.sh || true & sleep 20 && cd /commands \
    && ./grafana_setup.sh \
    && sleep 1

FROM grafana/grafana-oss
USER grafana
COPY --from=builder /usr/share/grafana /usr/share/grafana
ENTRYPOINT ["run.sh"]