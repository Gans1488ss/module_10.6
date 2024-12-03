                   # Урок 7
import datetime
import multiprocessing as mp
from PIL import Image
from queue import Empty

def resize_image(image_paths, pipe: mp.Pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image_resize((800, 600))
        pipe.send(image_path)
    stop_event.set()
def change_color(pipe):
    while not stop_event.is_set:
        image_path = pipe.recv()
        image = Image.open(image_path)
        image = image.convert("L")
        image.sale(image_path)

if __name__ == "__name__":
    data = []
    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event()
    for image in range(1, 10):
        data.append(f"./image/img_{image}.jpg")

    resize_proccess = mp.Proccess(target=resize_image, args=(data.conn1))
    change_proccess = mp.Proccess(target=change_color, args=(conn2, stop_event ))
    start = datetime.datetime.now()
    resize_proccess.start()
    change_proccess.start()

    resize_proccess.join()
    change_proccess.join()
    end = datetime.datetime.now()
    print(end - start)
