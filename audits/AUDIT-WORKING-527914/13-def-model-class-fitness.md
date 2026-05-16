# 13 - def-model-class-fitness

Segment: `01-aat-core/src/def-model-class-fitness.md` (`#def-model-class-fitness`)

Dependencies: `def-model-sufficiency`, already read. Dependency-order check passes.

## Segment Read

This segment defines $\mathcal F(\mathcal M)$ as the supremum of model sufficiency over a model class. It separates a bad current model from a bad representational class: low $S(M_t)$ can be a learning problem, while low $\mathcal F(\mathcal M)$ is structural inadequacy that parameter tuning cannot fix.

The key operational idea is the structural inadequacy condition $\mathcal F(\mathcal M) \lt 1-\varepsilon$, which triggers structural adaptation later.

## Predictions Vs Evidence

I predicted `model class fitness` would be the natural companion to model sufficiency. This segment confirms that. It also sharpens the bias/variance analogy: class fitness is about bias ceiling; instance sufficiency includes estimation quality.

## Cross-Segment Consistency

This segment depends cleanly on `#def-model-sufficiency`. It inherits the well-definedness and prediction-task relativity of $S$, though it does not restate all of those caveats. That is reasonable but worth remembering for downstream claims.

No contradiction.

## Naming Notes

`model class fitness` is acceptable but slightly biologically loaded. The segment's definition is "best achievable sufficiency within a model class," so "fitness" means representational adequacy ceiling, not evolutionary reproductive success. The term works because it is short and the formal definition controls it.

An alternative like `model class ceiling` would be more directly mathematical, but it would lose the sense that the class may or may not fit the environment. I would keep current unless a strong candidate exists.

`structural inadequacy` is also an important phrase. It may be a better name for the failure condition than for the quantity. If a target asks about model-class insufficiency, this segment partially grounds it but the structural-adaptation segment will likely be the defining home.

## What This Enables

This enables structural adaptation necessity: if the class's ceiling is below adequate sufficiency, no parameter update can solve the problem. It gives a formal route from persistent mismatch to changing model class.

For naming, it establishes a useful distinction:

- `model sufficiency`: current model's retained predictive information
- `model class fitness`: best possible sufficiency within representational class
- `structural inadequacy`: class-level failure condition

## Watchlist

- Candidates that rename this as "accuracy" or "capacity" without preserving sufficiency.
- Downstream uses that forget $\mathcal F$ is a supremum over representable models, not an easily observed quantity.
- Whether "fitness" collides with biological/evolutionary meanings in composition/logozoetic contexts.

## Wandering Thoughts

This is a small segment but a useful hinge. It gives the theory permission to say "learning harder will not help." That is a powerful diagnostic distinction in real systems, including AI agents and software teams.

The name `fitness` is a little risky but defensible. It says the class fits the prediction task. If the framework used "adequacy" everywhere it might be plainer, but "class fitness" is more speakable and pairs well with insufficiency/structural adaptation.

I also notice how much of AAD's diagnostic power comes from separating levels: model instance vs model class, adaptive scope vs agency, availability vs exploitation, sufficiency vs accuracy. Naming should preserve those separations rather than collapse them into broad "capability" terms.

The next segment should likely turn the low-fitness condition into a necessity result. If it does, I expect naming pressure around `structural adaptation`, `mismatch floor`, and perhaps `model-class insufficiency`.
