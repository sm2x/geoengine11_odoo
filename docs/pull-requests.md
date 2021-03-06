# Pull requests and reviews

Pull requests for new features are always proposed on `master`.

There are two exceptions for this rule:

* [patches for production releases](./releases.md#Versioning pattern) are created on dedicated branches using the naming scheme `patch-x.y.z`.
* large developments that must be developed aside the main branches during some time or branches that need consolidation before being merged in `master` may be done in separate `feature-xxx` branches.

In both cases, you should ask to the [Release Master](./releases.md#Release master) to create the required branch.

The pull requests must conform to the following points to be merged:

* The Travis build must be green
  * pep8 is checked
  * tests of local addons pass
* It contains tests
* The changelog is updated (one or a few lines added in the
  `unreleased` section of [HISTORY.rst](../HISTORY.rst))
* The [upgrade scripts](./upgrade-scripts.md) have been updated
* PR [automated quality checks](./pull-requests-quality-check.md) are passing
