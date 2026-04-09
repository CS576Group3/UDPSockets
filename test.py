import socket
import subprocess
import sys
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8888
BUFFER_SIZE = 1024
TIMEOUT = 3

TEST_CASES = [
    "Hello",
    "Hi",
]

JOKE_SUFFIX = " - I'm going to break your legs now!"


def run_server():
    ##start server.py as background process##
    try:
        process = subprocess.Popen([sys.executable, "server.py"])
        time.sleep(1)
        return process
    except Exception as e:
        print(f"Could not start server: {e}")
        return None


def stop_server(process):
    ##stop server.py as background process##
    if process is not None:
        process.terminate()
        process.wait()



def send_udp_message(message):
    ##send one UDP message and return the server response.##
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(TIMEOUT)

    try:
        client_socket.sendto(message.encode("ascii"), (SERVER_HOST, SERVER_PORT))
        response, _ = client_socket.recvfrom(BUFFER_SIZE)
        return response.decode("ascii")
    finally:
        client_socket.close()



def run_tests():
    ##run all test cases and print pass/fail results.##
    passed = 0
    failed = 0

    print("UDP Client-Server Automated Test")
    print("-" * 40)

    for i, test_message in enumerate(TEST_CASES, start=1):
        expected = test_message + JOKE_SUFFIX

        try:
            actual = send_udp_message(test_message)
            if actual == expected:
                print(f"Test {i}: PASS")
                print(f"  Sent:     {test_message}")
                print(f"  Received: {actual}")
                passed += 1
            else:
                print(f"Test {i}: FAIL")
                print(f"  Sent:      {test_message}")
                print(f"  Expected:  {expected}")
                print(f"  Received:  {actual}")
                failed += 1

        except socket.timeout:
            print(f"Test {i}: FAIL")
            print(f"  Sent: {test_message}")
            print("  Error: Timed out waiting for server response")
            failed += 1

        except Exception as e:
            print(f"Test {i}: FAIL")
            print(f"  Sent: {test_message}")
            print(f"  Error: {e}")
            failed += 1

        print()

    print("-" * 40)
    print(f"Total Passed: {passed}")
    print(f"Total Failed: {failed}")


if __name__ == "__main__":
    server_process = run_server()

    if server_process is None:
        print("Testing aborted: server could not be started.")
        sys.exit(1)

    try:
        run_tests()
    finally:
        stop_server(server_process)
