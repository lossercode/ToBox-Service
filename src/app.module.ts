import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AgentController } from './pages/agent/agent.controller';
import { AgentModule } from './pages/agent/agent.module';

@Module({
  imports: [AgentModule],
  controllers: [AppController, AgentController],
  providers: [AppService],
})
export class AppModule {}
