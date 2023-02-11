# Trainings on Git and GitHub

## Mermaid documentation

- [Mermaid live editor](https://mermaid.live/)
- [Gitgraph diagrams](https://mermaid.js.org/syntax/gitgraph.html)

## Mermaid example diagram

```mermaid
---
title: Example Git diagram
---
%%{init: { 'gitGraph': {'showBranches': true, 'rotateCommitLabel': true}} }%%

gitGraph
   commit
   commit
   branch develop
   checkout develop
   commit
   commit
   checkout main
   merge develop
   commit
   commit type: HIGHLIGHT tag: "v0.1.0"
   commit
```