# normalize nodes

This operation updates the identifiers on qgraph and kgraph nodes to their preferred identifiers, and adds equivalent identifiers in a property for knodes.  When two kgraph nodes normalize to the same  preferred identifier, the two knodes are merged.  The new node contain the union of the properties of the two original nodes.  All edges attached to either of the two original nodes are now subsequently attached to the new merged knode.  Qnodes are not merged, so that the structure of the query can be preserved.   The updates to kgraph node identifiers also necessitates the updating of result node bindings.

### examples

- [input](../examples/normalize_nodes/messages/01_prenormalized_message.json), [output](../examples/)
- [input](../examples/), [output](../examples/normalize_nodes/messages/02_postnormalized_message.json)

### input requirements

None

### output guarantees

None

### allowed changes

- modify qnodes
- modify knodes
- remove knodes
- modify kedges
- modify node bindings

### parameters

```yaml
{}
```
