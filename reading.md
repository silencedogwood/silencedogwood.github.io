---
layout: page 
title: Reading
publish: true
--- 

# Reading

Right now, mostly thinking about financial independence and freedom. 

::: {#favorites} 
Favorites
::: 

::: reading-list
#. *Harry Potter and the Methods of Rationality* by Eliezer Yudkowsky {% notes hpmor %}
#. *When Breath Becomes Air* by Paul Kalanithi
#. *Shoe Dog* by Phil Knight
#. *The Way to Love* by Anthony De Mello {% notes way_to_love %}
#. Scott Alexander's posts {% notes scott_alexander %}
#. "Humans are not automatically strategic" by Anna Salamon
#. ["Ted Kennedy's Eulogy for Robert Kennedy"](https://www.youtube.com/watch?v=aV0MKikJraE)
:::


::: {#now-reading}
Now Reading 
:::

::: reading-list 
#. *The Courage to Be Disliked* by Ichiro Kishimi
#. *Seeking Wisdom: From Darwin to Munger* by Peter Bevelin
#. *The Precipice: Existential Risk and the Future of Humanity* by Toby Ord
#. *The Fifteen Decisive Battles of the World* by Sir Edward Shepherd Creasy
#. *War and Peace* by Leo Tolstoy
#. *Gödel, Escher, Bach: An Eternal Golden Braid* by Douglas Hofstadter
#. *The End of Time: The Next Revolution in Physics* by Julian Barbour
#. *Only Words* by Catherine MacKinnon
:::

::: {#finished} 
Finished 
::: 

::: reading-list 
#. "When We Build" by Wilson Miner 
#. *The Lessons of History* by Will and Ariel Durant
#. *Quantum Computing Since Democritus* by Scott Aaronson {% notes democritus %}
#. *Hackers and Painters* by Paul Graham
#. *The Innovators* by Walter Isaacson
#. *Surely You're Joking Mr. Feynman* by Richard Feynman
#. "On Reading and Books" by Arthur Schopenhauer {% notes books %}
#. "Shut up and do the impossible!" by Eliezer Yudkowsky
#. "I Wasn't Prepared to Work" by Robert Smith
#. *Quantum Mechanics: The Theoretical Minimum* by Susskind and Friedman
#. "Becoming a magician" by Autotranslucence
#. "The Fable of the Dragon-Tyrant" by Nick Bostrom
#. *Sum: Forty Tales from the Afterlives* by David Eagleman
#. *Zero to One* by Peter Thiel and Blake Masters
#. *How to Take Smart Notes* by Sönke Ahrens {% notes smart_notes %}
#. *Lifespan: Why We Age and Why We Don't Have To* by David Sinclair {% notes lifespan-rough %}
#. *Ego is the Enemy* by Ryan Holiday {% notes ego %}
#. *The Rosie Project* by Graeme Simsion {% notes rosie %}
#. "Speed matters: Why working quickly is more important than it seems" by James Somers
#. *The Rosie Effect* by Graeme Simsion
#. "Principles of Effective Research" by Michael Nielsen
#. *Inadequate Equilibria* by Eliezer Yudkowsky {% notes equilibria %}
#. *Founders at Work* by Jessica Livingston 
#. *The Ballad of Songbirds and Snakes* by Suzanne Collins
#. *Conspiracy* by Ryan Holiday {% notes conspiracy %}
#. *Early Retirement Extreme* by Jacob Lund Fisker
#. *Six of Crows* by Leigh Bardugo
#. *Crooked Kingdom* by Leigh Bardugo
#. "Advice for ambitious teenagers" by Laura Deming
#. "How to Understand Things" by Nabeel Qureshi
:::

::: {#anti-library} 
Anti-Library [\[?\]](https://fs.blog/2013/06/the-antilibrary/)
:::

::: reading-list 
#. *What Mad Pursuit* by Francis Crick
#. *Reasons and Persons* by Derek Parfit
#. *On What Matters* by Derek Parfit
#. *Give War and Peace a Chance* by Andrew Kaufman
#. *The Death of Ivan Ilyich* by Leo Tolstoy 
#. *A Confession* by Leo Tolstoy 
#. *Anna Karenina* by Leo Tolstoy 
#. *Proofs from THE BOOK* by Martin Aigner
#. *Spark* by John Ratey 
#. *The Sense of Style* by Steven Pinker
#. *ANSI Common Lisp* by Paul Graham 
#. *Ideas and Opinions* by Albert Einstein 
#. *Einstein: His Life and Universe* by Walter Isaacson {% notes einstein %}
#. *Linear Operators for Quantum Mechanics* by Thomas Jordan
#. *Algorithms* by Dasgupta, Papadimitriou, and Vazirani
#. *On Writing* by Stephen King
#. *Moonwalking with Einstein* by Joshua Foer
#. *Story of Philosophy* by Will Durant
#. *The Art of Profitability* by Adrian Slywotzky
#. *E-Myth Revisited* by Michael Gerber (1!)
#. *The Ultimate Sales Machine* by Chet Holmes (2!)
#. *On Writing Well* by William Zinsser
#. *Benjamin Franklin: An American Life* by Walter Isaacson
#. *Meditations* by Marcus Aurelius
#. *The Man Who Loved Only Numbers* by Paul Hoffman
#. *The Four Steps to the Epiphany* by Steve Blank
#. *The Innovator's Solution* by Clayton Christensen
#. *Autobiography of a Yogi* by Paramahansa Yogananda
#. *How Buildings Learn* by Stewart Brand
#. *How to Read a Book: The Classic Guide to Intelligent Reading* by Mortimer Adler and Charles van Doren 
#. *Draft No.4: On the Writing Process* by John McPhee
#. *The Elements of Style [Illustrated]* by William Strunk Jr., E.B. White, and Maira Kalman
#. *Man: The Moral Animal* by Robert Wright
#. *The Adapted Mind* by Barkow, Cosmides, and Tooby
#. *Inward Bound: Of Matter and Forces in the Physical World* by Abraham Pais
#. *Handbook of the Biology of Aging, Eighth Edition* by Matt Kaeberlein and George Martin
:::

<!-- This script is for notes expand/collapse functionality -->
<script>
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
      coll[i].innerHTML = "[+]";
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
          content.style.maxHeight = null;
          this.innerHTML = "[+]";
        } else {
          content.style.maxHeight = content.scrollHeight + "px";
          this.innerHTML = "[–]";
        }
      });
    }
</script>
