import cohere
import json

class TextParser:

    def __init__(self, co):
        self.co = co
        print("Built parser")
    
    def parse_text(self, text):
        chat_history = [
            {
                "user_name": "User",
                "text": 
                """
                You are given the following JSON pattern to split texts:

                {
                "paragraphs":
                [
                {
                "paragraph_number": 1,
                "paragraph_text": "paragraph_1"
                },
                {
                "paragraph_number": 2,
                "paragraph_text": "paragraph_2"
                },
                ...
                ]
                }

                So, following the previous JSON format, you will read the following text and convert it into paragraphs of at least 30 words each:

                Sheets of empty canvas
                Untouched sheets of clay
                Were laid spread out before me
                As her body once did

                All five horizons
                Revolved around her soul
                As the earth to the sun
                Now the air I tasted and breathed
                Has taken a turn

                Oh, and all I taught her was everything
                Oh, I know she gave me all that she wore

                And now my bitter hands
                Chafe beneath the clouds
                Of what was everything
                Oh, the pictures have
                All been washed in black
                Tattooed everything

                I take a walk outside
                I'm surrounded by some kids at play
                I can feel their laughter
                So, why do I sear?

                Oh, and twisted thoughts that spin round my head
                I'm spinning, oh, I'm spinning
                How quick the sun can drop away?

                And now my bitter hands
                Cradle broken glass
                Of what was everything
                All the pictures have
                All been washed in black
                Tattooed everything
                All the love gone bad
                Turned my world to black
                Tattooed all I see
                All that I am
                All that I'll be, yeah

                I know someday you'll have a beautiful life
                I know you'll be a star
                In somebody else's sky, but why? Why? Why
                Can't it be, oh, can't it be mine?

                Now, provide the split using the previous JSON format.}
                """
            },
            {
                "user_name": "Chatbot",
                "text": 
                """
                {
                "paragraphs":
                [
                {
                "paragraph_number": 1,
                "paragraph_text": "Sheets of empty canvas Untouched sheets of clay Were laid spread out before me As her body once did"
                },
                {
                "paragraph_number": 2,
                "paragraph_text": "All five horizons Revolved around her soul As the earth to the sun Now the air I tasted and breathed Has taken a turn"
                }
                {
                "paragraph_number": 3,
                "paragraph_text": "All five horizons Revolved around her soul As the earth to the sun Now the air I tasted and breathed Has taken a turn"
                },
                {
                "paragraph_number": 4,
                "paragraph_text": "All five horizons Revolved around her soul As the earth to the sun Now the air I tasted and breathed Has taken a turn"
                },
                {
                "paragraph_number": 5,
                "paragraph_text": "And now my bitter hands Chafe beneath the clouds Of what was everything Oh, the pictures have All been washed in black Tattooed everything
                }
                ]
                }
                """
            }
            
        ]
        message = "Do the same for " + text

        response = self.co.chat(
            message=message,
            chat_history=chat_history
        )

        texts = response.text
        texts = texts.replace('\n', '')
        texts = texts.replace('```', '')
        texts = texts.replace('json', '')
        texts = json.loads(texts)

        answer = []
        for paragraph in texts['paragraphs']:
            answer.append(paragraph['paragraph_text'])
        
        return answer

