# Python SonarQube Example

Full Blog Post:

https://ranbook.cloud/posts/python-sonarqube-coverage-tests

## Steps

`docker network create sonar-network`

```
docker run \
--network sonar-network \
--name sonarqube \
-p 9000:9000 \
sonarqube:10.6-community
```

`python3 -m venv .penvsonar`
`source .penvsonar/bin/activate`

`pip3 install -r requirements-test.txt`

`pylint src -r n --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --output=pylint-report.txt`

`bandit -r ./src --format json --output bandit-report.json`

`coverage run -m pytest --junitxml=pytest-report.xml tests`

`coverage xml --omit="tests/*"`

```
docker run \
--network sonar-network \
--rm \
-e SONAR_HOST_URL="http://sonarqube:9000"  \
-e SONAR_TOKEN="xxxxxx" \
-v "${PWD}:/usr/src" \
sonarsource/sonar-scanner-cli
```