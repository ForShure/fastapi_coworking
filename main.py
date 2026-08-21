import asyncio
import grpc

from src.domain.entities import Workplace
from src.infrastructure.database import async_session_maker
from src.infrastructure.repositories import SqlAlchemyWorkplaceRepository
from src.presentation.grpc_server import GrpcCoworkingHandler
from protos.coworking_pb2_grpc import add_CoworkingServiceServicer_to_server

async def serve():
    async with async_session_maker() as session:
        db_repository = SqlAlchemyWorkplaceRepository(session)
        my_workplace = Workplace(
            id=1,
            name="Стол у окна",
        )
        await db_repository.save(my_workplace)

    server = grpc.aio.server()
    add_CoworkingServiceServicer_to_server(GrpcCoworkingHandler(async_session_maker), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())

