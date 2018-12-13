import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-generate-bad',
  templateUrl: './generate-bad.component.html',
  styleUrls: ['./generate-bad.component.scss']
})
export class GenerateBadComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  ComeBack() {
    this.router.navigate(['/start']);
  }
}
