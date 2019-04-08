import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {ITaskList} from '../../shared/models/models';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http:HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]>
  {
    return this.get('http://127.0.0.1:8000/api/task_lists',{})
  }

  getTasks(t_ls: ITaskList): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/task_lists/${t_ls.id}/tasks`, {});
  }
}
