
''' Timed input test
    Use threads to process user input, with a timeout
    Written by PM 2Ring 2017.07.20
'''

from threading import Thread, Timer, Event

# Some ANSI/VT100 Terminal Control Escape Sequences
CSI = '\x1b['
SAVE_CURSOR = CSI + 's'
UNSAVE_CURSOR = CSI + 'u'
GOTO_START = CSI + '1G'


def shutdown(finished):
    print('\nShutting down')
    finished.set()
    # Save data, etc.


def countdown(delay):
    print(SAVE_CURSOR, GOTO_START, '%2d' % delay, UNSAVE_CURSOR,
          sep='', end='', flush=True)
    if delay:
        countdown.timer = Timer(1, countdown, (delay-1,))
        countdown.timer.start()


def process_input(delay, shutdown_timer):
    countdown(delay)
    s = input('%2d > ' % delay)
    countdown.timer.cancel()
    shutdown_timer.cancel()
    print(s.upper())


def main():
    delay = 5
    finished = Event()
    while not finished.isSet():
        shutdown_timer = Timer(delay, shutdown, (finished,))
        shutdown_timer.start()
        worker = Thread(target=process_input, args=(delay, shutdown_timer,))
        worker.setDaemon(True)
        worker.start()
        shutdown_timer.join()
        print("hello")


if __name__ == '__main__':
    main()
