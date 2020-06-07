# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import stream_pb2 as stream__pb2


class StreamStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Detection = channel.unary_stream(
                '/Stream/Detection',
                request_serializer=stream__pb2.StreamRequest.SerializeToString,
                response_deserializer=stream__pb2.StreamFrame.FromString,
                )


class StreamServicer(object):
    """The greeting service definition.
    """

    def Detection(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Detection': grpc.unary_stream_rpc_method_handler(
                    servicer.Detection,
                    request_deserializer=stream__pb2.StreamRequest.FromString,
                    response_serializer=stream__pb2.StreamFrame.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Stream', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Stream(object):
    """The greeting service definition.
    """

    @staticmethod
    def Detection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Stream/Detection',
            stream__pb2.StreamRequest.SerializeToString,
            stream__pb2.StreamFrame.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
