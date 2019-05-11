import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {ITaskList,ITask,IToken} from '../../shared/models/models';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';


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

  getTasks(t_ls: ITaskList): Promise<ITask[]>
  {
    return this.get(`http://localhost:8000/api/task_lists/${t_ls.id}/tasks`, {});
  }


  createTaskList(name: any): Promise<ITaskList>
  {
    return this.post(`http://localhost:8000/api/task_lists`, {name: name});
  }

  updateTaskList(category: ITaskList): Promise<ITaskList>
  {
    return this.put(`http://localhost:8000/api/task_lists/${category.id}/`, {name: category.name});
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }


  auth(login:any,password:any): Promise<IToken>
  {
    return this.post('http://localhost:8000/login/',{
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/logout/', {});
  }




}
