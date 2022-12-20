from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
   BatchSpanProcessor,
   ConsoleSpanExporter,
)
provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("rootSpan"):
    with tracer.start_as_current_span("childSpan"):
        with tracer.start_as_current_span("GrandchildSpan"):
           print("Hello world!")

with tracer.start_as_current_span("rootSpan1"):
    print("Hello world! - 1")