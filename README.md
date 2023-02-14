<img src="./assets/logo.png" alt="ClamAV Mirror Server" height="150" />
  
This is a mirror server for the ClamAV virus database. It is a simple Python script that downloads the latest database from the ClamAV project and serves it to clients.

---

## Environment variables

| Variable             | Default | Description                                     |
| -------------------- | ------- | ----------------------------------------------- |
| HTTP_PORT            | 8000    | The port the server will listen on              |
| UPDATE_EVERY_N_HOURS | 24      | How often the database should be updated        |
| DATA_DIR             | /data   | The directory where the database will be stored |

## Kubernetes deployment example

An example of a kubernetes deployment of the service can be found here [deployment.yaml](./examples/deployment.yaml).

**OBS** remeber to update the image repository.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.
