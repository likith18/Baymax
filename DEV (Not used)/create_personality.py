# from hume import HumeVoiceClient, VoiceConfig
#
# client = HumeVoiceClient("HUME_API_KEY_HERE")
# config: VoiceConfig = client.create_config(
#     name=f"//user given personality name ",
#     prompt="{user prompt}",
# )
# print("Created config: ", config.id)
#


from hume import VoiceConfig, HumeVoiceClient


def create_personality_config(client):
    name = input("Enter the personality name: ")
    prompt = input("Enter the prompt: ")
    config: VoiceConfig = client.create_config(
        name=name,
        prompt=prompt,
    )
    print("Created config:", config.id)
