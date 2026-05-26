# Module 3 — Reflection

**Team name**: BUI_Nhat
**Branch**: `module-03/BUI_Nhat`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:*
The gateway gives clients one stable entry point instead of forcing them to know where every service runs. Without it, the client would need to remember multiple ports and URLs like user-service on 8001, game-service on 8002, and activity-service on 8003. The client would also need to handle failures and routing logic itself. With the gateway, all requests go through port 8000, which simplifies the frontend and hides the internal architecture. It also makes it easier to add authentication, logging, or rate limiting later without changing every service.


---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:*
The validation call is critical because an activity should not be created for a user that does not exist. If user-service is temporarily slow or unavailable, retrying gives the system another chance before failing the request. Without validation, the database could end up with invalid activities linked to fake users.
The game enrichment call is optional because the activity itself is still valid even if game-service is down. The user can still log that they played something, and the missing game details can be handled later. Returning `"game": null` allows the system to degrade gracefully instead of blocking the entire request because of one unavailable service.


---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:*
The biggest risk is that one slow or failing service can slow down the entire request chain. Since activity-service depends on user-service and sometimes game-service, the final response time becomes limited by the slowest service involved. If one service takes 3 seconds to respond, the user experiences the whole request as slow, even if the other services are fast. In larger systems this can create cascading failures where one overloaded service causes delays and timeouts across the entire platform.

---

*Keep this file. You will refer back to it during the oral presentation.*
