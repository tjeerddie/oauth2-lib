# OAuth2-lib
This Project contains an Mixin class that wraps an openapi-codegen python client, to inject Opentelemetry spans
and api call retries. It also contains a number of FastAPI dependancies which enables Policy enforcement offloading
to Open Policy Agent.

The project contains a number of OIDC classes that are tailored to the SURF environment.


## Installation
This can be done as follows:

#### Step 1:
First install flit to enable you to develop on this repository
```bash
pip install flit
```
#### Step 2:

To install all development dependancies
```bash
flit install --deps develop --symlink
```

With this way all requirements are installed for testing and development.

## Development
Depending on the feature type, run bumpversion (patch|minor|major) to increment the version you are working on

## For MAC users looking and experimenting with Opentelemetry (OTEL)
https://github.com/jaegertracing/jaeger-client-node/issues/124#issuecomment-324222456
