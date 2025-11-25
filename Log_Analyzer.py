#!/usr/bin/env python3
import re
import argparse
from collections import defaultdict, Counter
from datetime import datetime

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.stats = {
            'total_lines': 0,
            'errors': 0,
            'warnings': 0,
            'info': 0,
            'debug': 0,
            'critical': 0
        }
        self.error_messages = []
        self.warning_messages = []
        self.timestamps = []
        
    def analyze(self):
        """Main analysis function"""
        try:
            with open(self.log_file, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    self._analyze_line(line.strip(), line_num)
            
            self._generate_report()
            
        except FileNotFoundError:
            print(f"Error: File '{self.log_file}' not found!")
        except Exception as e:
            print(f"Error analyzing file: {e}")
    
    def _analyze_line(self, line, line_num):
        """Analyze a single log line"""
        self.stats['total_lines'] += 1
        
        # Check for different log levels (case insensitive)
        line_lower = line.lower()
        
        if 'error' in line_lower:
            self.stats['errors'] += 1
            self.error_messages.append((line_num, line))
        
        elif 'warning' in line_lower or 'warn' in line_lower:
            self.stats['warnings'] += 1
            self.warning_messages.append((line_num, line))
        
        elif 'info' in line_lower:
            self.stats['info'] += 1
        
        elif 'debug' in line_lower:
            self.stats['debug'] += 1
        
        elif 'critical' in line_lower or 'fatal' in line_lower:
            self.stats['critical'] += 1
            self.error_messages.append((line_num, line))
        
        # Extract timestamp if present
        self._extract_timestamp(line)
    
    def _extract_timestamp(self, line):
        """Extract timestamp from log line"""
        # Simple timestamp pattern (adjust based on your log format)
        timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
        match = re.search(timestamp_pattern, line)
        if match:
            self.timestamps.append(match.group())
    
    def _generate_report(self):
        """Generate a comprehensive analysis report"""
        print("\n" + "=" * 60)
        print("LOG FILE ANALYSIS REPORT")
        print("=" * 60)
        print(f"File analyzed: {self.log_file}")
        print(f"Analysis time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)
        
        # Basic statistics
        print("\nBASIC STATISTICS:")
        print("-" * 30)
        for level, count in self.stats.items():
            print(f"{level.replace('_', ' ').title():<15}: {count}")
        
        # Error details
        if self.error_messages:
            print(f"\nERRORS FOUND ({len(self.error_messages)}):")
            print("-" * 30)
            for line_num, error in self.error_messages[:5]:  # Show first 5 errors
                print(f"Line {line_num}: {error[:80]}...")
            if len(self.error_messages) > 5:
                print(f"... and {len(self.error_messages) - 5} more errors")
        
        # Warning details
        if self.warning_messages:
            print(f"\nWARNINGS FOUND ({len(self.warning_messages)}):")
            print("-" * 30)
            for line_num, warning in self.warning_messages[:3]:  # Show first 3 warnings
                print(f"Line {line_num}: {warning[:80]}...")
        
        # Timestamp analysis
        if self.timestamps:
            print(f"\nTIMESTAMP ANALYSIS:")
            print("-" * 30)
            print(f"Lines with timestamps: {len(self.timestamps)}")
            if len(self.timestamps) >= 2:
                print(f"First entry: {self.timestamps[0]}")
                print(f"Last entry:  {self.timestamps[-1]}")
        
        # Summary
        print("\n" + "=" * 60)
        error_rate = (self.stats['errors'] / self.stats['total_lines']) * 100 if self.stats['total_lines'] > 0 else 0
        print(f"SUMMARY: Error rate: {error_rate:.2f}%")
        
        if self.stats['errors'] == 0 and self.stats['warnings'] == 0:
            print("✅ Log file looks clean!")
        elif self.stats['errors'] > 10:
            print("🚨 High number of errors detected!")
        elif self.stats['warnings'] > 20:
            print("⚠️  Many warnings detected - review recommended")

def main():
    parser = argparse.ArgumentParser(description='Analyze log files for errors and patterns')
    parser.add_argument('logfile', nargs='?', default='sample.log', 
                       help='Path to the log file (default: sample.log)')
    parser.add_argument('--output', '-o', help='Output file for the report')
    
    args = parser.parse_args()
    
    # Create analyzer and run analysis
    analyzer = LogAnalyzer(args.logfile)
    analyzer.analyze()
    
    # TODO: Add output to file functionality
    if args.output:
        print(f"\nReport would be saved to: {args.output}")

if __name__ == "__main__":
    main()
