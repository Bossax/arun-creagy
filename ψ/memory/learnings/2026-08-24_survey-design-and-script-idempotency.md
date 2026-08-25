# Lesson: Measurement validity before interaction cost; build update paths alongside create paths

**Context**: Building a Google Apps Script feedback form for CRDB's 26th dissemination event, grounded in a 41-slide Thai deck. Iterated through three rounds of Boss's critique.

## Lesson 1 — Interrogate measurement validity before interaction cost

When designing a survey/feedback instrument, the first question should be "does this metric discriminate between good and bad outcomes, and does it map to a decision" — not "how many taps/pages does this cost the respondent." A generic "relevance to your work" 1-5 scale, asked of an audience pre-selected for relevance, produces a ceiling effect (everyone rates 4-5) and no decision-usable signal, no matter how cheap it is to answer. It took a direct challenge ("is that response gonna give useful information?") to surface this — I should default to asking it myself before optimizing interaction cost. The fix that emerged (priority × completeness as a paired measure, read as a quadrant) was strictly more useful *and* no more expensive to answer than the flawed single-dimension version — validity and cost aren't always in tension.

## Lesson 2 — Build create/update symmetry into scripts from the start

Any script whose job is to instantiate a persistent resource (`FormApp.create()`, a repo scaffold, a deployment) will predictably need an "update the existing one" mode the moment someone iterates on the design after the first successful run — which for an iterative design process is almost immediately. Retrofitting this (extracting a shared `buildFormBody()`, adding `FORM_ID`-based `openById` + delete-and-rebuild) is mechanical but adds churn and requires the user to re-diagnose "wait, doesn't this just make a duplicate?" Building both paths in the first pass — even if the update path isn't used until later — avoids that friction and the restructuring risk once the user is already depending on IDs from the create run.

## Tags
survey-design, google-apps-script, idempotency, measurement-validity, ceiling-effect, iterative-design
