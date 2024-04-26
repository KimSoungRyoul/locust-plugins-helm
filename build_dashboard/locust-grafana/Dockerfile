FROM sky5367/locust-grafana-base:3 as builder

FROM grafana/grafana-oss
USER grafana
COPY --from=builder /var/lib/grafana /var/lib/grafana
#ENTRYPOINT ["run.sh"]