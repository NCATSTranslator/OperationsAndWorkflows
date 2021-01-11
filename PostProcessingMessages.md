# Post-processing Messages

## Motivation

Many operations are meant to be applied to Messages with existing knowledge graphs and results:
* "filter"
* "score"
* ...

The service performing these operations must have access to the pre-filled "original" Message, which is potentially large. Messages have been observed in the wild up to ~500MB.

The original Message may or may not have originated with the same service performing the post-processing.

## Desiderata

[in no particular order]
* data transfer over HTTP should be minimized
* system (Translator) complexity should be minimized
  * client/server interfaces should be simple
  * there should be only one way to do things
  * there should be few request/response communications between components
* client/server complexity should be low
  * processing and storage requirements should be minimized

## Mechanisms

* **TRAPI (1.0) message:** The original Message is passed from the client to the server via HTTP.
* **URI reference:** The original Message is stored on the originating service in case the same service is called upon to perform post-processing.

## Considerations

* The original Message **must** be passed if the post-processing service is different from the originating service.
* The use of URI references:
  * allows saving some bandwidth in cases where:
    * subsequent operations are performed by the same service
    * the chain of operations cannot be combined into one request
  * makes the client/server interface (i.e. TRAPI) more complex
  * allows two ways to initiate a post-processing operation, sometimes
  * expands server processing requirements somewhat
  * expands server storage requirements, potentially a lot
    * Services must store results for some time (how long?) and recall them on demand.
  * expands client processing/storage requirements a bit
    * Clients must remember who knows what and figure out when they need to send URIs vs. Messages.

## Conclusions and Rationale

* Support for verbose passing of the original Message is required. Otherwise operations cannot be chained using multiple services.
* Support for URI references would provide some bandwidth savings sometimes at the cost of:
  * substantial server storage requirements
  * moderate server processing requirements
  * light client storage requirements?
  * moderate client processing requirements
  * moderate increase in interface/system complexity
