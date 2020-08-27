**Notes: assume all are direct quotations**

*Preface* 

Thesis: QM isn't about matter, energy, waves, or particles. It's about 
information and probabilities and observables, and how they relate to each 
other. 

QM might be counterintuitive, but we should ask: *where* did my intuition go 
wrong such that I wouldn't be able to intuit or predict QM? 

It might be the case that QM is inherently ununderstandable. Aaronson says if 
that's true, he *doesn't care* about QM. He'll go do something else. It's like 
flunking him without telling him how to improve or even telling him that he 
can't improve. 

Here's the book's perspective on this: QM is a generalization of the laws of 
probability that use the 2-norm instead of the 1-norm, and complex numbers. 
We can study it *completely independently* from its use in physics. Whiel QM 
was invented to explain physical phenomena, *now* we can explain it as part of 
the history of ideas in math, logic, computing, and philosophy about the limits 
of the knowable. 

*Chapter 1: Atoms and the void* 

Democritus writes a dialogue between Intellect and Senses: 

Intellect: 
> By convention there is sweetness, by convention bitterness, by convention 
color, *in reality* only atoms and the void. 

Senses: 
> Foolish Intellect! Do you seek to overthrow us, while it is from us that you 
take your evidence? 

I think I'm missing a few layers of detail but I think Aaronson is says this is 
a metaphor for QM because: QM says atoms and the void evolve unitarily but 
measuring collapses this. This measurement part is weird: what even counts as a 
measurement? Removing it would make things cleaner from a physics standpoint. 
But we have *data* so we know this isn't true and that measurements exist ie 
Nature does unitary evolution until someone looks and then it does something 
else! 

We can classify interpretations of QM by what they say about the idea of 
"putting yourself in a coherent superposition." Copenhagen sweeps this under 
the rug - there's a line separating quantum systems and measurements. 
Many-world and Bohmian mechanics try to answer the question. 

*Chapter 2: Sets* 

Math is the foundation of thought, and set theory is the foundation of math. 

The language we'll use to talk about sets is called first-order logic. 

**Rules of first-order logic**: the rules all govern how to construct sentences
that are *valid* ie tautologically true. 

1. Propositional tautologies: $A \cup \neg A$ and also $\neg( A \cap \neg A )$
2. Modus ponens: if $A$ is valid and $A$ implies $B$ is valid, $B$ is valid. 
3. Equality rules: $x = y, x = y$ implies $y = x $
4. Change of variables: swapping the variables doesn't change anything 
5. Quantifier elimination: if $\forall x, A(x)$ is valid, then $A(y)$ is valid 
for any $y$ 
6. Quantifier addition: if $A(y)$ is valid for any $y$, then $\forall x, A(x)$ 
is valid 
7. Quantifier rules: if $\neg( \forall x, A(x) )$ is valid, then there exists 
some $x$ such that $\neg(A(x))$ is valid. 

**Peano axioms for nonnegative integers in first-order logic**

Let $S(x) = x + 1$. 

1. Zero exists: $\exists z: \forall x, S(x) \neq z$
2. Every integer has at most one predecessor: $\forall x,y : S(x) = S(y) 
\Rightarrow x = y$

The nonnegative integers are a *model* for the Peano axioms, ie some set that 
satisfies the axioms. 


While all these axioms seem unnecessary, they'll become our guide when we move 
past the integers. 

**Axioms of set theory: Zermelo-Fraenkel axioms** 

1. Empty set: $\exists x: \forall y y \notin x$
2. Extensionality: if 2 sets contain the same members, they're equal 
3. Pairing: $\forall x, y: \exists z = \{ x, y \}$ such that $\forall w: w \in 
z \iff w = x \cup x = y$
4. Union: for all sets $x$ there exists a set equal to the union of all sets 
in $x$
5. Existence of infinite sets: there exists a set $x$ that contains the empty 
set and that contains $\{ y \}$ for every $y \in x$
6. Power set: for all sets $x$ there exists a set consisting of subsets of $x$ 
7. Replaement: For all sets $x$, there exists a set $z = \{ A(y) | y \in x \}$
8. Foundation: All nonempty sets $x$ have a member $y$ such that for all $z$, 
either $z \notin x$ or $z \notin y$ ie any set cannot exist in *both* $x$ and 
$y$. This rules out infinite sets like $\{ \{ \{ ... \infty ... \} \} \}$. 

Cardinalities: all the finite ones (natural numbers), then $\aleph\_0$ (aleph 
zero). 

Natural numbers, integers, and rational numbers have cardinality $\aleph\_0$. 
(We say two sets have the same cardinality if there's a one-to-one mapping.) 

There are infinitely many infinities. PROOF: 

Suppose we have an infinite set $A$. We'll create set $B$ such that $B$ has 
more elements than $A$. 

Let $B$ be the set of all subsets of $A$, guaranteed to exist by Power Set 
axiom. Suppose we can map each $a \in A$ to an element $f(a) \in B$. 

Let $S \subseteq A$ consist of *every* $a$ not contained in $f(a)$. 

Since $S$ is a subset of $A$, $S \subseteq B$, which means that $f(a) = S$ for 
some $a$. 

$a \in S$ can't be true because $f(a) = S$ and $a \in S$, but $S$ contains only 
elements $a$ such that $a \notin f(a)$. 

$a \notin S$ can't be true because then $a \notin f(a)$ so it should be in $S$. 

Contradiction. So $B$ must have larger cardinality than $A$. 

Define $\omega$ to be greater than all the natural numbers. What comes after 
$\omega$? Well $\omega + 1$, $\omega + 2$, ..., $2\omega$, ..., $3\omega$, ..., 
$\omega^2$, ..., $\omega^3$, ..., $\omega^2$, ..., $\omega^3$, ..., 
$\omega^\omega$, ..., $\omega^{\omega^\omega}$, ... 

These are called the ordinal numbers. ANy set of ordinal numbers has a first 
ordinal number that comes after everything in the set. 

Similarly, the ordinal numbers are well-ordered, which means every subset of 
of a set of ordinal numbers has a minimum element. 

Consider the set of all ordinal numbers with countably many predecessors. The 
successor to this set must have a cardinality of predecessors that is 
uncountable, or it would have been in the set. Call this cardinality 
$\aleph\_1$. 

By this logic, the set of cardinalities is also well-ordered. 

Starting with $\aleph\_0$, what is the next cardinality? 
    Well we know how to construct $\aleph\_1$ from above.  
    What about cardinality of *sets* of all integers, $2^{\aleph\_0}$? This is 
the set of all real numbers. 

Are they equal? This was Hilbert's first problem in 1900. 

Cantor believed there was no intermediate infinity. He conjectured the Continuum 
Hypothesis: there is no set $S$ such that 

$\aleph\_0 < | S | < 2^{\aleph\_0}$. 

There's another statement that hasn't been proved from ZF axioms: the Axiom of 
Choice, which states if you have a (possibly infinite) set of sets, then it's 
possible to form a new set choosing one item from each set. The Banach-Tarski 
paradox uses this axiom to prove it's possible to cut a solid sphere into 
finite pieces and reconstruct them to create a solid sphere 1000 times bigger. 

The heart of why the Axiom of Choice has such huge consequences is that it 
asserts certain sets exist without providing a rule for constructing them. 

AC is equal the statement that every set can be well-ordered. Here's why: 

Well-ordering -> AC: we can well-order our set of sets then pick the item 
in each set with lowest ordinal. 

AC -> well-ordering: for all proper subsets $B \subset A$, use AC to pick 
an element $f(B) \in A - B$. Then we can well-order by: 
    - $s\_0 = f( {} ) \in A$ 
    - $s\_1 = f( {s\_0} ) \in A - s\_0$ 
    - $s\_2 = f( {s\_0, s\_1} ) \in A - s\_0 - s\_1$ 
    - ... 

Even if $A$ is infinite, it must have some fixed infinite cardinality, so this 
ordering can't go on forever. (Why not?) 

There are difficulties with CH. 

Suppose we want a union of open intervals that cover every rational point. Does 
the sum of lengths of intervals have to be infinite? No! The rational numbers 
are countable, so we can enumerate them and then surround them with interval 
$\epsilon / 2^i$ for the $i$th rational number. (How does this use CH?) 
