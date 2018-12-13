import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-readme',
  templateUrl: './readme.component.html',
  styleUrls: ['./readme.component.scss']
})
export class ReadmeComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  ComeBack() {
    this.router.navigate(['/start']);
  }
}
