Step 1: Install prometheus
<code>
wget https://github.com/prometheus/prometheus/releases/latest/download/prometheus-linux-amd64.tar.gz
tar xvf prometheus-linux-amd64.tar.gz
cd prometheus-*
</code>
* configure prometheus.yml
<code>
global:
  scrape_interval: 15s
scrape_configs:
  - job_name: 'jenkins'
    metrics_path: "/prometheus"
    static_configs:
      - targets: ['AWS_public-ip:8080'] 
</code>
* start prometheus
<code>./prometheus --config.file=prometheus.yml</code>

<hr>

Step 2: Configure Jenkins for metrics
* Install the Prometheus Plugin in Jenkins
    <code>manage jenkins > install Prometheus metrics plugin > restart jenknins</code>
* Enable Prometheus Metrics in Jenkins
    <code>manage jenkins > configure system > enable prometheus metrics endpoint</code> it will listen on http://aws-ip:8080/prometheus

<hr>

step 3: Set Up Grafana
<code>
wget https://dl.grafana.com/oss/release/grafana-10.0.0.linux-amd64.tar.gz
tar -zxvf grafana-10.0.0.linux-amd64.tar.gz
cd grafana-10.0.0
./bin/grafana-server
</code>
* open http://aws-ip:3000, login using admin/admin as credentials
* <code>configuration > data sources > set url http://aws-ip:9090 ></code>click ''save & test''
* import prebuild jenkins dashboard
    <code>configuration > dashboards > import > DashBoard id/ .json file</code> >> load

<hr>

