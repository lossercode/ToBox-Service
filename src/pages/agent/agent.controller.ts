import { Controller, Get } from '@nestjs/common';
import { Response } from '../../common/response';

@Controller('agent')
export class AgentController {
  @Get()
  getAgentList() {
    return Response.success(' hello ');
  }
}
