# Email Simulator

A Python exercise from the freeCodeCamp Python curriculum that simulates a basic email system using object-oriented programming.

## Overview

The Email Simulator allows users to send, receive, read, list, and delete emails through a simple command-line simulation.

The program models users, emails, and inboxes as separate objects that interact with one another.

## Concepts Practiced

* Object-oriented programming (OOP)
* Classes and objects
* Constructors and instance attributes
* Methods
* Object composition
* Lists and list manipulation
* Conditional logic
* Input validation
* Date and time handling with `datetime`
* String formatting
* Special methods such as `__str__`
* Encapsulation of related functionality

## Classes

### `Email`

Represents an individual email and stores information such as the sender, receiver, subject, body, timestamp, and read status.

### `User`

Represents a user who can send emails, check their inbox, read emails, and delete emails.

### `Inbox`

Manages a user's collection of emails and provides functionality for receiving, listing, reading, and deleting emails.

## Features

* Send emails between users
* Automatically receive emails in the recipient's inbox
* List received emails
* Track read and unread status
* Display the complete contents of an email
* Delete emails
* Validate email indexes
* Record the time an email was received

## Example

The program creates two users, Tory and Ramy, and simulates an exchange of emails between them.

```text
Email sent from Tory to Ramy!

Email sent from Ramy to Tory!

Ramy's Inbox:

Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: ...

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: ...
Body: Hi Ramy, just saying hello!
------------

Email deleted.
```

## Status

Completed as a progress exercise while working through the freeCodeCamp Python curriculum.
