def send_smishing_sms(phone_number, fake_link):
    print("----- Simulated SMS -----")
    print(f"To: {phone_number}")
    print(f"Message: Your account has been suspended. Verify immediately at: {fake_link}")
    print("-------------------------")
