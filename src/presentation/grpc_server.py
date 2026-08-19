from protos import coworking_pb2
from protos import coworking_pb2_grpc
from src.application.usecases import BookWorkplaceUseCase
from src.infrastructure.repositories import InMemoryWorkplaceRepository

class GrpcCoworkingHandler(coworking_pb2_grpc.CoworkingServiceServicer):
    def BookWorkplace(self, request, context):
        try:
            workplace_id = request.workplace_id
            repo = InMemoryWorkplaceRepository()
            use_case = BookWorkplaceUseCase(repo=repo)
            use_case.execute(workplace_id=workplace_id)
            return coworking_pb2.BookResponse(
                success=True,
                message='The place is reserved')
        except Exception:
            return coworking_pb2.BookResponse(
                success=False,
                message='Something went wrong'
            )

