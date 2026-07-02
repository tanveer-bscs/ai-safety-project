from datetime import datetime
# AI Safety Checker - Version 2

with open("unsafe_words.txt", "r") as file:
    unsafe_words = file.read().splitlines()

prompt = input("Enter your prompt: ").lower()

prompt_length = len(prompt)

found_words = []

for word in unsafe_words:
    if word in prompt:
        found_words.append(word)

if len(found_words) == 0:
    score = 100
    print("\n✅ Safe Prompt")
    print("Safety Score: 100/100")
    print("Verdict: Safe")

else:
    score = 100 - (len(found_words) * 20)

    if score < 0:
        score = 0
    print("\n❌ Unsafe Prompt")
    print("\nUnsafe Words Found:")

    for word in found_words:
        print("-", word)
    print("Total Unsafe Words:", len(found_words))
    print("Prompt Length:", len(prompt))
    print("\nSafety Score:", score, "/100")

    if score >= 80:
        print("Verdict: Low Risk")
    elif score >= 50:
        print("Verdict: Medium Risk")
    else:
        print("Verdict: High Risk")

# Save result to history.txt
with open("history.txt", "a") as file:
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file.write(f"Date & Time: {current_time}\n")
    file.write(f"Prompt: {prompt}\n")
    file.write(f"Prompt Length: {prompt_length}\n")
    file.write(f"Total Unsafe Words: {len(found_words)}\n")
    file.write(f"Safety Score: {score}/100\n")

    if len(found_words) == 0:
        file.write("Verdict: Safe\n")
    elif score >= 80:
        file.write("Verdict: Low Risk\n")
    elif score >= 50:
        file.write("Verdict: Medium Risk\n")
    else:
        file.write("Verdict: High Risk\n")

    file.write("-" * 30 + "\n")