from protos import coworking_pb2
from protos import coworking_pb2_grpc
from src.application.usecases import BookWorkplaceUseCase
from src.infrastructure.repositories import SqlAlchemyWorkplaceRepository

class GrpcCoworkingHandler(coworking_pb2_grpc.CoworkingServiceServicer):
    def __init__(self, session_maker):
        self.session_maker = session_maker

    async def BookWorkplace(self, request, context):
        try:
            async with self.session_maker() as session:
                repo = SqlAlchemyWorkplaceRepository(session)
                use_case = BookWorkplaceUseCase(repo=repo)
                await use_case.execute(workplace_id=request.workplace_id)
                return coworking_pb2.BookResponse(
                    success=True,
                    message='The place is reserved')
        except Exception as e :
            return coworking_pb2.BookResponse(
                success=False,
                message='Something went wrong'
            )

