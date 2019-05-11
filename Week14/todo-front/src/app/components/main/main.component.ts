import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../../shared/services/provider.service';
import { ITaskList, ITask } from '../../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css', 'bootstrap.css']
})
export class MainComponent implements OnInit {

  public t_ls: ITaskList[] = []
  public tasks: ITask[] = []
  public logged = false;
  public login:any = '';
  public password:any = '';
  public name: any = '';


  constructor(private provider: ProviderService) { }


    ngOnInit()
    { 
     
        if (this.logged) {
        this.provider.getTaskLists().then(res => {this.t_ls = res;});
        }

    }


  

  getTasks(t_ls: ITaskList)
  {
    this.provider.getTasks(t_ls).then(res => {this.tasks = res;});

  }

  updateTaskList(tl: ITaskList) {
    this.provider.updateTaskList(tl).then(res => {
      console.log(tl.name + ' updated');
    });
  }
  deleteTaskList(tl: ITaskList) {
    this.provider.deleteTaskList(tl.id).then(res => {
      console.log(tl.name + ' deleted');
      this.provider.getTaskLists().then(r => {
        this.t_ls = r;
      });
    });
  }
  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.t_ls.push(res);
      });
    }
  }



  auth() {
          if(this.login!=='' && this.password!==''){
            this.provider.auth(this.login,this.password).then(r => {
              localStorage.setItem('token', r.token);
          });
          this.logged=true;
          this.provider.getTaskLists().then(res => {this.t_ls = res;});
            }
    }


  logout() {
  this.provider.logout().then(res => { localStorage.clear();this.logged = false;});
    }
}
