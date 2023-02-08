# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Jeremy Pogue
- Kaelyn Cho
- Note: We worked independently, but helped each other when needed

## Lab Question Answers

Answer for Question 1: 

RESTful APIs are scalable because of specific architecture requirements that can expedite or even eliminate some client-server interactions.
All RESTful APIs, by definition, must be stateless and cacheable. In calling RESTful APIs "stateless", we are saying that each client-server
interaction is independent of the others (a client-server interaction never transitions the API to a different state). This is helpful for 
scaleability because stateless APIs don't have to store the outcomes/results of prior interactions, resulting in a lower load. In calling
RESTful APIs "cacheable", we are saying that frequently-referenced information can be stored on the client (or some intermediary
close to the client) rather than the server. This is helpful for scaleability because, for frequently-referenced information, cacheable APIs
don't have to communicate directly between the client and the server.

Answer for Question 2:

The AWS article defines resources as "the information that different applications provide to their clients". They are the pieces of information
provided to the client by the server. Therefore, in the example of our mail server, the resources would be the emails and their corresponding data. 
For instance, when the user provides the inbox command, the resources sent from the server to the user are the body, id, recipient, sender, and 
subject of each of their received emails. 

Answer for Question 3:

Our mail server doesn't use the PUT method, which is used to update the resources currently held on the server. This method could potentially be used
for edit functionality, where a user could edit the content of their email after "sending" it. It could also allow for a primitive version of "forwarding",
where the user could edit the "recipients" list of an email to include an additional recipient. 

Answer for Question 4:

Source: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key
Intuitively, API keys allow the creators of the API to track their users. If an API contains sensitive information, it might require an API key to prevent
random users from accessing its data. Additionally, the creators of an API might also want to track the number of times that a user gets information
from the API. This might help identify suspicious activity, and also be used to charge users that pull from the API for some business use. For instance,
the OpenWeather API charges $0.0015 per API call above the daily limit of 1,000.