import asyncio
import grpc

from src.domain.entities import Workplace
from src.infrastructure.repositories import InMemoryWorkplaceRepository
from src.presentation.grpc_server import GrpcCoworkingHandler
from protos.coworking_pb2_grpc import add_CoworkingServiceServicer_to_server

async def serve():
    repo = InMemoryWorkplaceRepository()
    repo.save(Workplace(
        id=1,
        name="Стол у окна"
    ))
    server = grpc.aio.server()
    add_CoworkingServiceServicer_to_server(GrpcCoworkingHandler(repo), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())

