# Module 2 — Reflection

**Team name**: BUI_Nhat
**Branch**: `module-02/BUI_Nhat`
**Submitted**: before Module 3 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You built a service with distinct layers: models, schemas, repository, service, and routes — each with a single responsibility.

**Why not just put everything in one file and call it done?**

Think about what happens six months later when someone new joins the team, or when you need to swap SQLite for PostgreSQL. What does the layered structure protect you from?

> *Your answer:*
Keeping everything in one file may work for a very small project, but it becomes difficult to maintain as the system grows. The layered structure separates responsibilities so each part of the service has a clear role.
For example, the repository layer handles database queries, while the service layer contains business logic. This makes the code easier to understand for new developers because they immediately know where to look when changing a feature or fixing a bug.
The structure also makes future changes safer. If we later switch from SQLite to PostgreSQL, most changes would stay inside the database and repository layers without affecting the API routes or schemas. Without separation, changing one part of the system could accidentally break unrelated features.

---


---

## 2. Your choice

Each service owns its data exclusively — no other service is allowed to touch its database directly.

**Pick one entity your service owns (e.g. `User`, `Game`). What would go wrong if another service could write to that table directly?**

Give a concrete scenario, not a general principle.

> *Your answer:*
The "Game" entity should only be owned by the game-service.
For example, imagine the recommendation-service could directly write into the "games" table. A bug in the recommendation logic could accidentally modify or delete game information while generating recommendations.
This would create inconsistent data across the platform. Users might suddenly see incorrect game titles, genres, or missing entries. By forcing all changes to go through the game-service API, the service keeps control over validation and business rules.


---

## 3. The tradeoff

You now have models, schemas, a repository, a service, and routes — five layers for what is essentially a CRUD service.

**For a system this small, what is the cost of all this structure?**

And at what point does the complexity start to pay off? Where is the tipping point?

> *Your answer:*
The main cost of this structure is extra complexity and boilerplate. For a small CRUD service, creating models, schemas, repositories, services, and routes can feel repetitive and slower than writing everything in one file.
Debugging can also require jumping through multiple layers before finding the source of a problem.
However, the structure starts paying off once the project grows beyond a few endpoints or multiple developers start working on it. At that point, clean separation makes the codebase easier to scale, test, and maintain without turning into a monolith full of tightly coupled logic.

---

*Keep this file. You will refer back to it during the oral presentation.*
