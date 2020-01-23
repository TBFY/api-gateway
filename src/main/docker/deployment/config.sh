curl -X POST https://localhost:8001/apis/3b279925-6fff-48be-95de-14662686d973/plugins \
  --data "name=zipkin"  \
  --data "config.http_endpoint=http://zipkin:9411/api/v2/spans" \
  --data "config.sample_ratio=1.0"
