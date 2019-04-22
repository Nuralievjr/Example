import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../../shared/services/provider.service';
import { ITaskList, ITask } from '../../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public t_ls: ITaskList[] = []
  public tasks: ITask[] = []
  constructor(private provider: ProviderService) { }

  ngOnInit()
  {

  this.provider.getTaskLists().then(res => {this.t_ls = res;});

  }

  getTasks(t_ls: ITaskList)
  {
    this.provider.getTasks(t_ls).then(res => {this.tasks = res;});

  }

}
