## Grafana의 기본 이미지를 사용
#FROM grafana/grafana-oss
#
## 대시보드 JSON 파일을 이미지에 추가
#COPY ./locust-dashboard-json/ /etc/grafana/provisioning/dashboards/locust-dashboard-json/
#
## 대시보드 프로비저닝 설정 파일 추가
#COPY dashboards.yml /etc/grafana/provisioning/dashboards/
#
## 필요한 추가 설정을 여기에 수행
## 예: 플러그인 설치
#RUN grafana-cli plugins install grafana-clock-panel
#
## Grafana 시작
#ENTRYPOINT [ "/run.sh" ]


FROM grafana/grafana-oss
USER root
COPY *.sh /commands/
RUN chown -R grafana /commands
RUN apk add curl jq
USER grafana
RUN /run.sh & sleep 10 && cd /commands \
    && ./grafana_setup.sh \
    && sleep 1
#
#
#FROM grafana/grafana-oss
#USER grafana
#COPY --from=builder /usr/share/grafana /usr/share/grafana
#ENTRYPOINT ["run.sh"]