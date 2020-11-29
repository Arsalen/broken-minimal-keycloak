# DevOps assignment

Minimal environment with `keycloak` and a custom `python` app behind
`nginx`, in `docker`, orchestrated with `docker-compose`.

## Development

1. Start the environment: `docker-compose up -d`.
2. Create a new user in the `keycloak` admin: http://localhost/keycloak/admin
    * username `admin` and password in `.env` file below.
    * Once logged in, click on `Users` > `Add user`, fill `Username` then click `Save` > `Credentials`, fill `Password` and `Password Confirmation` then click `Set Password` and confirm.
```INI
KEYCLOAK_PASSWORD=<KEYCLOAK_PASSWORD>
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
```
### Endpoints

1. http://localhost/: "Hello world!" index page.
2. http://localhost/login: redirects to `keycloak` auth.
3. http://localhost/auth/callback: `keycloak` callback after login.

### Fixed issues

1. The docker-compose `entrypoint` and `command` directives override the Dockefile `ENTRYPOINT` instruction, so the app is launched using `python3 app.py` command rather than `gunicorn` Web Server Gateway Interface.
2. The app's login is broken because of a typo `/loogin` in the web service endpoint (`app.py` file).
3. Connections to the `keycloak` endpoints fail because nginx redirects to the wrong port (`8090` rather than `8080`).
4. Improvements in the build process and the Dockerfile
    * Decouple server block from Nginx main configuration.
    * Create a working directory to contain the application source and requirements rather than `/var/www/`.
    * Refactor gunicorn parameters into a separate python module `/config/gunicorn.py` and initiate them through environment variables.
    * Set metadata for the image using `LABEL`.
    * Edit service dependencies (`depends_on` directives) within the docker-compose.

## Author
@arsalen ([github](https://github.com/Arsalen), [medium](https://medium.com/@arsalen), [linkedin](https://www.linkedin.com/in/arsalen-hagui-506979123/))