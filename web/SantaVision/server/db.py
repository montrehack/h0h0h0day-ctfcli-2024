import uuid

class VideoRepository:
    def __init__(self):
        self.videos = {
            "flag1": "42b376b9-32f5-5bf3-a131-bbdba4b2614f",
            "flag2": "2aa2f106-d72a-5b44-82f8-8d2453e018d2",
            "flag3": "b4f3c547-fe93-5fd9-8418-51d705fee48e",
            # Swapped for uuid to name mapping
            "42b376b9-32f5-5bf3-a131-bbdba4b2614f": "flag1",
            "2aa2f106-d72a-5b44-82f8-8d2453e018d2": "flag2",
            "b4f3c547-fe93-5fd9-8418-51d705fee48e": "flag3",
        }
    