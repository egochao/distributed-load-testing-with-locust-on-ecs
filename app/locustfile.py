from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def send_simple_request(self):
        # self.client.get("/")
        with open("data/jfk.flac", "rb") as f:
            audio_bytes = f.read()

        response = self.client.post(
            "/predictions/whisper_base", 
            files={"data": audio_bytes}
            )
        transcription =  response.text.lower()
        print(transcription)
