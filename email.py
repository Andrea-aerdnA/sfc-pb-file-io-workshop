
class Email:
  def __init__(self, id, sender, recipient, subject, body):
    self.id = id
    self.sender = sender
    self.recipient = recipient
    self.subject = subject
    self.body = body

  def to_dict(self):
    return {
      "id": self.id,
      "sender": self.sender,
      "recipient": self.recipient,
      "subject": self.subject,
      "body": self.body
    }
