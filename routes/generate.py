from flask import request, jsonify
from google import genai
from google.genai import types
import os

def generate_routes(app):
    @app.route('/generate', methods=['POST'])
    def generate():
        try:
            app.logger.info("Generate route accessed.")
            client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
            model = "gemini-2.0-flash"

            input_text = request.json.get("input")
            if not input_text:
                app.logger.warning("Missing 'input' in request body.")
                return jsonify({"error": "Missing 'input' in request body"}), 400

            app.logger.debug(f"Input received: {input_text}")

            contents = [
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(text=input_text),
                    ],
                ),
            ]
            tools = [
                types.Tool(google_search=types.GoogleSearch())
            ]
            generate_content_config = types.GenerateContentConfig(
                tools=tools,
                response_mime_type="text/plain",
            )

            response_text = ""
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=generate_content_config,
            ):
                response_text += chunk.text

            app.logger.info("Response successfully generated.")
            return jsonify({"response": response_text})

        except Exception as e:
            app.logger.error(f"An error occurred: {e}", exc_info=True)
            return jsonify({"error": "An unexpected error occurred. Please contact an admin."}), 500
