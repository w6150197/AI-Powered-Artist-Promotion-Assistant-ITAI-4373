import time
from monitor.source import get_new_post
from ai_engine.scorer import score_opportunity
from ai_engine.responder import generate_response
from database.db import save_opportunity

print("\n🎨 AI-Powered Artist Assistant — Live Monitoring Started\n")

while True:
    post = get_new_post()

    print("\n------------------------------")
    print("📥 New Incoming Post:")
    print(post)

    score = score_opportunity(post["text"])
    print(f"\n🎯 AI Opportunity Score: {score}")

    if score < 0.5:
        print("\n⚠️ Low score — skipping.")
        time.sleep(2)
        continue

    ai_reply = generate_response(post["text"])
    print("\n🤖 Suggested AI Response:")
    print(ai_reply)

    save_opportunity(post, score, ai_reply)
    print("💾 Saved to opportunities.json")

    time.sleep(2)
