from cvdupdate.cvdupdate import CVDUpdate
import threading, logging, os, sys, time, http.server, socketserver, pathlib

HTTP_PORT = int(os.getenv("HTTP_PORT", 8000))
UPDATE_EVERY_N_HOURS = int(os.getenv("UPDATE_EVERY_N_HOURS", 24))
DATA_DIR = os.getenv("DATA_DIR", "/data")

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
)


def update():
    m = CVDUpdate(config="", verbose=False)
    m.db_dir = pathlib.Path(DATA_DIR)

    errors = m.db_update()
    if errors > 0:
        logging.error("Update failed with %d errors", errors)
        pass


def updater():
    while True:
        logging.info("Performing update!")
        update()
        time.sleep(60 * 60 * UPDATE_EVERY_N_HOURS)


def server():
    os.chdir("/data")
    with socketserver.TCPServer(
        ("", HTTP_PORT), http.server.SimpleHTTPRequestHandler
    ) as httpd:
        logging.info("Now serving at port TCP %d", HTTP_PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    logging.info("Performing initial update")

    updateThread = threading.Thread(target=updater)
    updateThread.start()

    logging.info("Starting web server")

    serverThread = threading.Thread(target=server)
    serverThread.start()

    logging.info("Ready!")

    updateThread.join()
    serverThread.join()
