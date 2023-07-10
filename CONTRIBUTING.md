Contribution guidelines
=======================

Please not that this project follows the [Contributor Covenant Code of
Conduct](https://www.contributor-covenant.org/version/1/4/code-of-conduct/). By
participating in this project you agree to abide by its terms.

Contribution to the Awesome List
--------------------------------

There are two ways (described below) to suggest data changes.

- Via a Pull Request (PR) to the README.md
- By making changes to the MongoDB database

All changes to data must adhere to the following guidelines:

- Changes must include at least basic information that make the scope and the
  content of the changes clear. It is recommended to say why you suggest them.  
- Links to resources must be valid, relevant, safe and appropriate.

### Suggest changes

You can suggest changes by editing the Awesome List in `README.md` via GitHub's
web interface or via a text editor.

Submit your changes as a PR. It is recommended to add a few words to
explain why you're proposing the changes.

> If you submit a change that is accepted, please note that the project owner
  will add it to the database and not only to the Awesome List text file.

### Modify the database

*All the content from the Awesome List comes from the database. The list is*
*generated automatically from it.*

Data can be modified using the tool Turn/IP (see Turn/IP's documentation in
`srcs/README.md`).

> You can also update the JSON files directly but that is not recommended.

So that the changes made in Turn/IP can be committed, you'll have to export
the databases:

```
python turn-ip.py --mongoexport
```

Submit the databases `protocols.json` and `links.json` as a PR.

Contribution to Turn/IP
-----------------------

*Turn/IP is the tool used to generate the Awesome List. It also has features to*
*simplify researches on industrial network protocols.*

Contributing to Turn/IP means making changes to the **code** (not the
database). Please ensure your PR adheres to the following guidelines:

- We like clean code and expect contributions to be PEP-8 compliant as much as
  possible (even though we don't test for it).
- New code should be readable easily and maintainable.
- If you need to use "and" while explaining what your function does, you can
  probably split it.
